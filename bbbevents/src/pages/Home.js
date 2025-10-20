import React, { useState, useEffect } from 'react';
import { supabase } from '../supabaseClient';
import { Link } from 'react-router-dom';
import { Container, Typography, Grid, Card, CardContent, Button, CardActions, CardMedia, Chip } from '@mui/material';
import banner from '../images/bbb_g.png';

function Home() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchEvents();
  }, []);

    const fetchEvents = async () => {
    const { data, error } = await supabase
      .from('events')
      .select('*, rsvps(id)') // Select rsvps to count them
      .order('date', { ascending: true });
    if (error) console.error('Error fetching events:', error);
    else {
      const eventsWithSeats = data.map(event => {
        const rsvpsCount = event.rsvps ? event.rsvps.length : 0;
        return { ...event, seats_left: event.total_seats - rsvpsCount };
      });
      setEvents(eventsWithSeats);
    }
  };

  const truncateDescription = (description) => {
    if (description.length > 120) {
      return description.substring(0, 120) + '…';
    }
    return description;
  };

  return (
    <Container sx={{ py: 4 }} maxWidth="lg">
      <Typography variant="h2" align="center" color="primary.main" gutterBottom sx={{ mb: 6 }}>
        Upcoming Events
      </Typography>
      <Grid container spacing={4}>
        {events.map((event) => (
          <Grid item key={event.id} xs={12} sm={6} md={4}>
            <Card
              sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                boxShadow: '0 4px 8px 0 rgba(0,0,0,0.2)',
                transition: '0.3s',
                '&:hover': {
                  boxShadow: '0 8px 16px 0 rgba(0,0,0,0.2)',
                },
              }}
            >
              <CardMedia
                component="img"
                height="200"
                image={banner}
                alt={event.name}
              />
              <CardContent sx={{ flexGrow: 1 }}>
                <Typography gutterBottom variant="h5" component="h2" color="primary">
                  {event.name}
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                  {new Date(event.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
                </Typography>
                <Chip
                  label={`Seats Left: ${event.seats_left} / ${event.total_seats}`}
                  color={event.seats_left === 0 ? 'error' : (event.seats_left <= 5 ? 'warning' : 'success')}
                  sx={{ mb: 2, fontSize: '0.8rem' }}
                />
                <Typography variant="body1">
                  {truncateDescription(event.description)}
                </Typography>
              </CardContent>
              <CardActions sx={{ justifyContent: 'center', mb: 1 }}>
                <Button component={Link} to={`/event/${event.slug}`} variant="contained" color="secondary">
                  View Details & RSVP
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default Home;
