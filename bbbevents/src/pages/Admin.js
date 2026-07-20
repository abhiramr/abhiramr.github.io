import React, { useState, useEffect } from 'react';
import { supabase } from '../supabaseClient';
import { Container, TextField, Button, Typography, Box, Tabs, Tab, List, ListItem, ListItemText, IconButton, Modal, Select, MenuItem, InputLabel, FormControl, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import CancelIcon from '@mui/icons-material/Cancel';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          {children}
        </Box>
      )}
    </div>
  );
}

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

function Admin() {
  const [value, setValue] = useState(0);
  const [eventName, setEventName] = useState('');
  const [eventDate, setEventDate] = useState('');
  const [eventDescription, setEventDescription] = useState('');
  const [totalSeats, setTotalSeats] = useState('');
  const [events, setEvents] = useState([]);
  const [open, setOpen] = useState(false);
  const [currentEvent, setCurrentEvent] = useState(null);
  const [rsvps, setRsvps] = useState([]);
  const [selectedEvent, setSelectedEvent] = useState('');
  const [maxTicketsPerRsvp, setMaxTicketsPerRsvp] = useState('');

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    const { data, error } = await supabase.from('events').select('*');
    if (error) console.error('Error fetching events:', error);
    else setEvents(data);
  };

  const fetchRsvps = async (eventId) => {
    const { data, error } = await supabase.from('rsvps').select('id, name, email, event_id, num_tickets').eq('event_id', eventId);
    if (error) console.error('Error fetching rsvps:', error);
    else setRsvps(data);
  };

  const handleCancelRsvp = async (rsvpId, eventId) => {
    if (window.confirm('Are you sure you want to cancel this RSVP?')) {
      // Delete the RSVP
      const { error: deleteError } = await supabase
        .from('rsvps')
        .delete()
        .eq('id', rsvpId);

      if (deleteError) {
        console.error('Error canceling RSVP:', deleteError);
        alert('Error canceling RSVP. See console for details.');
      } else {
        // Increment seats_left in the events table
        const { data: eventData, error: fetchEventError } = await supabase
          .from('events')
          .select('seats_left')
          .eq('id', eventId)
          .single();

        if (fetchEventError) {
          console.error('Error fetching event for seat update:', fetchEventError);
          alert('RSVP canceled, but failed to update seats count.');
        } else {
          const newSeatsLeft = eventData.seats_left + 1;
          const { error: updateError } = await supabase
            .from('events')
            .update({ seats_left: newSeatsLeft })
            .eq('id', eventId);

          if (updateError) {
            console.error('Error updating seats left:', updateError);
            alert('RSVP canceled, but failed to update seats count.');
          } else {
            alert('RSVP canceled successfully!');
            fetchRsvps(selectedEvent); // Refresh the current RSVP list
            fetchEvents(); // Refresh the main events list to update seat counts
          }
        }
      }
    }
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  
  const handleEventSelect = (e) => {
    setSelectedEvent(e.target.value);
    fetchRsvps(e.target.value);
  };

  const generateSlug = (name) => {
    return name
      .toLowerCase()
      .replace(/[^a-z0-9\s-]/g, '') // Remove special characters except spaces and hyphens
      .replace(/\s+/g, '-') // Replace spaces with hyphens
      .replace(/-+/g, '-'); // Replace multiple hyphens with a single hyphen
  };

  const handleCreateSubmit = async (e) => {
    e.preventDefault();
    const slug = generateSlug(eventName);
    const { data, error } = await supabase
      .from('events')
      .insert([{ name: eventName, date: eventDate, description: eventDescription, total_seats: totalSeats, seats_left: totalSeats, slug: slug, max_tickets_per_rsvp: maxTicketsPerRsvp }]);

    if (error) {
      console.error('Error creating event:', error);
      alert('Error creating event. See console for details.');
    } else {
      console.log('Event created:', data);
      alert('Event created successfully!');
      setEventName('');
      setEventDate('');
      setEventDescription('');
      setTotalSeats('');
      fetchEvents(); // Refresh the list
    }
  };

  const handleEdit = (event) => {
    setCurrentEvent(event);
    setEventName(event.name);
    setEventDate(event.date);
    setEventDescription(event.description);
    setTotalSeats(event.total_seats);
    setMaxTicketsPerRsvp(event.max_tickets_per_rsvp);
    setOpen(true);
  };

  const handleUpdateSubmit = async (e) => {
    e.preventDefault();
    const slug = generateSlug(eventName);
    const { data, error } = await supabase
      .from('events')
      .update({ name: eventName, date: eventDate, description: eventDescription, slug: slug, max_tickets_per_rsvp: maxTicketsPerRsvp })
      .eq('id', currentEvent.id);

    if (error) {
      console.error('Error updating event:', error);
      alert('Error updating event. See console for details.');
    } else {
      console.log('Event updated:', data);
      alert('Event updated successfully!');
      setOpen(false);
      fetchEvents(); // Refresh the list
    }
  };

  const handleDelete = async (eventId) => {
    if (window.confirm('Are you sure you want to delete this event?')) {
      const { data, error } = await supabase.from('events').delete().eq('id', eventId);
      if (error) {
        console.error('Error deleting event:', error);
        alert('Error deleting event. See console for details.');
      } else {
        console.log('Event deleted:', data);
        alert('Event deleted successfully!');
        fetchEvents(); // Refresh the list
      }
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={handleChange} aria-label="admin tabs">
          <Tab label="Create Event" {...a11yProps(0)} />
          <Tab label="Manage Events" {...a11yProps(1)} />
          <Tab label="View RSVPs" {...a11yProps(2)} />
        </Tabs>
      </Box>
      <TabPanel value={value} index={0}>
        <Typography variant="h5" component="h2" gutterBottom>
          Create a New Event
        </Typography>
        <form onSubmit={handleCreateSubmit}>
          <TextField
            label="Event Name"
            variant="outlined"
            fullWidth
            margin="normal"
            value={eventName}
            onChange={(e) => setEventName(e.target.value)}
          />
          <TextField
            label="Event Date"
            type="date"
            variant="outlined"
            fullWidth
            margin="normal"
            InputLabelProps={{ shrink: true }}
            value={eventDate}
            onChange={(e) => setEventDate(e.target.value)}
          />
          <TextField
            label="Event Description"
            variant="outlined"
            fullWidth
            margin="normal"
            multiline
            rows={4}
            value={eventDescription}
            onChange={(e) => setEventDescription(e.target.value)}
          />
          <TextField
            label="Total Seats"
            type="number"
            variant="outlined"
            fullWidth
            margin="normal"
            value={totalSeats}
            onChange={(e) => setTotalSeats(e.target.value)}
          />
          <TextField
            label="Max Tickets Per RSVP"
            type="number"
            variant="outlined"
            fullWidth
            margin="normal"
            value={maxTicketsPerRsvp}
            onChange={(e) => setMaxTicketsPerRsvp(e.target.value)}
          />
          <Button type="submit" variant="contained" color="primary" fullWidth>
            Create Event
          </Button>
        </form>
      </TabPanel>
      <TabPanel value={value} index={1}>
        <Typography variant="h5" component="h2" gutterBottom>
          Edit or Delete an Existing Event
        </Typography>
        <List>
          {events.map((event) => (
            <ListItem
              key={event.id}
              secondaryAction={
                <>
                  <IconButton edge="end" aria-label="edit" onClick={() => handleEdit(event)}>
                    <EditIcon />
                  </IconButton>
                  <IconButton edge="end" aria-label="delete" onClick={() => handleDelete(event.id)}>
                    <DeleteIcon />
                  </IconButton>
                </>
              }
            >
              <ListItemText
                primary={event.name}
                secondary={new Date(event.date).toLocaleDateString()}
              />
            </ListItem>
          ))}
        </List>
      </TabPanel>
      <TabPanel value={value} index={2}>
        <Typography variant="h5" component="h2" gutterBottom>
          View Event RSVPs
        </Typography>
        <FormControl fullWidth>
          <InputLabel id="event-select-label">Select Event</InputLabel>
          <Select
            labelId="event-select-label"
            id="event-select"
            value={selectedEvent}
            label="Select Event"
            onChange={handleEventSelect}
          >
            {events.map((event) => (
              <MenuItem key={event.id} value={event.id}>{event.name}</MenuItem>
            ))}
          </Select>
        </FormControl>
        <Table sx={{ mt: 4 }}>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Email</TableCell>
              <TableCell>Tickets</TableCell>
              <TableCell>Action</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rsvps.map((rsvp, index) => (
              <TableRow key={index}>
                <TableCell>{rsvp.name}</TableCell>
                <TableCell>{rsvp.email}</TableCell>
                <TableCell>{rsvp.num_tickets}</TableCell>
                <TableCell>
                  <IconButton edge="end" aria-label="cancel" onClick={() => handleCancelRsvp(rsvp.id, rsvp.event_id)}>
                    <CancelIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TabPanel>
      <Modal
        open={open}
        onClose={() => setOpen(false)}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Edit Event
          </Typography>
          <form onSubmit={handleUpdateSubmit}>
            <TextField
              label="Event Name"
              variant="outlined"
              fullWidth
              margin="normal"
              value={eventName}
              onChange={(e) => setEventName(e.target.value)}
            />
            <TextField
              label="Event Date"
              type="date"
              variant="outlined"
              fullWidth
              margin="normal"
              InputLabelProps={{ shrink: true }}
              value={eventDate}
              onChange={(e) => setEventDate(e.target.value)}
            />
            <TextField
              label="Event Description"
              variant="outlined"
              fullWidth
              margin="normal"
              multiline
              rows={4}
              value={eventDescription}
              onChange={(e) => setEventDescription(e.target.value)}
            />
            <TextField
              label="Total Seats"
              type="number"
              variant="outlined"
              fullWidth
              margin="normal"
              value={totalSeats}
              onChange={(e) => setTotalSeats(e.target.value)}
            />
            <TextField
              label="Max Tickets Per RSVP"
              type="number"
              variant="outlined"
              fullWidth
              margin="normal"
              value={maxTicketsPerRsvp}
              onChange={(e) => setMaxTicketsPerRsvp(e.target.value)}
            />
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Update Event
            </Button>
          </form>
        </Box>
      </Modal>
    </Container>
  );
}

export default Admin;
            
