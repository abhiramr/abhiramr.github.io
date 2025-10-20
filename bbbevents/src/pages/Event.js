import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { supabase } from '../supabaseClient';
import ReactMarkdown from 'react-markdown';
import { Container, Typography, Box, TextField, Button, Paper, Grid, Chip } from '@mui/material';
import EventIcon from '@mui/icons-material/Event';

function Event() {
  const { id } = useParams();
  const [event, setEvent] = useState(null);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    fetchEvent();
  }, [id]);

  const fetchEvent = async () => {
    const { data, error } = await supabase
      .from('events')
      .select('*, rsvps(id)') // Select rsvps to count them
      .eq('id', id)
      .single();
    if (error) console.error('Error fetching event:', error);
    else {
      // Calculate seats_left based on total_seats and actual rsvps count
      const rsvpsCount = data.rsvps ? data.rsvps.length : 0;
      setEvent({ ...data, seats_left: data.total_seats - rsvpsCount });
    }
  };

  const handleRsvp = async (e) => {
    e.preventDefault();

    if (event.seats_left <= 0) {
      alert('Sorry, this event is full!');
      return;
    }

    // First, insert the RSVP
    const { data: rsvpData, error: rsvpError } = await supabase
      .from('rsvps')
      .insert([{ event_id: id, name, email }]);

    if (rsvpError) {
      console.error('Error RSVPing:', rsvpError);
      alert('Error RSVPing. See console for details.');
    } else {
      console.log('RSVP successful:', rsvpData);

      // Then, decrement seats_left in the events table
      const newSeatsLeft = event.seats_left - 1;
      const { error: updateError } = await supabase
        .from('events')
        .update({ seats_left: newSeatsLeft })
        .eq('id', id);

      if (updateError) {
        console.error('Error updating seats left:', updateError);
        alert('RSVP successful, but failed to update seats count.');
      } else {
        alert('Thank you for RSVPing!');
        setEvent(prevEvent => ({ ...prevEvent, seats_left: newSeatsLeft }));
        setName('');
        setEmail('');
      }
    }
  };

  if (!event) {
    return <Typography>Loading event...</Typography>;
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 6 }}>
      <Paper elevation={0} sx={{ p: { xs: 2, md: 5 }, backgroundColor: '#f9f9f9' }}>
        <Grid container spacing={5}>
          <Grid item xs={12} md={7}>
            <Typography variant="h3" component="h1" gutterBottom color="primary">
              {event.name}
            </Typography>
            <Chip 
              icon={<EventIcon />} 
              label={`Date: ${new Date(event.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}`}
              sx={{ mb: 3, fontSize: '1rem' }}
            />
            <Box sx={{ my: 2, '& a': { color: 'secondary.main' }, lineHeight: '1.7' }}>
              <ReactMarkdown>{event.description}</ReactMarkdown>
            </Box>
            <Typography variant="body2" color="text.secondary" sx={{ mt: 2 }}>
              Seats Left: {event.seats_left} / {event.total_seats}
            </Typography>
          </Grid>
          <Grid item xs={12} md={5}>
            <Box sx={{ p: 3, backgroundColor: '#fff', border: '1px solid', borderColor: 'grey.300', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
              <Typography variant="h5" component="h2" gutterBottom align="center" color="primary">
                RSVP for this Event
              </Typography>
              <form onSubmit={handleRsvp}>
                <TextField
                  label="Your Name"
                  variant="filled"
                  fullWidth
                  margin="normal"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
                <TextField
                  label="Your Email"
                  type="email"
                  variant="filled"
                  fullWidth
                  margin="normal"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
                <Button type="submit" variant="contained" color="secondary" size="large" sx={{ mt: 2, width: '100%' }} disabled={event.seats_left <= 0}>
                  {event.seats_left <= 0 ? 'Event Full' : 'Confirm Your Seat'}
                </Button>
              </form>
            </Box>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
}

export default Event;
