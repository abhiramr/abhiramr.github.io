import React from 'react';
import { HashRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import Event from './pages/Event';
import AdminLogin from './pages/AdminLogin';
import { createTheme, ThemeProvider, CssBaseline, Container } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: {
      main: '#264653',
    },
    secondary: {
      main: '#e76f51',
    },
    background: {
      default: '#fdfdfd',
    },
  },
  typography: {
    fontFamily: 'Roboto, sans-serif',
    h1: {
      fontFamily: 'Georgia, serif',
      fontSize: '2.5rem', // Reduced from default 6rem
    },
    h2: {
      fontFamily: 'Georgia, serif',
      fontSize: '2rem', // Reduced from default 3.75rem
    },
    h3: {
      fontFamily: 'Georgia, serif',
      fontSize: '1.75rem', // Reduced from default 3rem
    },
    h4: {
      fontFamily: 'Georgia, serif',
      fontSize: '1.5rem', // Reduced from default 2.125rem
    },
    h5: {
      fontFamily: 'Georgia, serif',
      fontSize: '1.25rem', // Reduced from default 1.5rem
    },
    h6: {
      fontFamily: 'Georgia, serif',
      fontSize: '1rem', // Reduced from default 1.25rem
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router basename="/bbbevents">
        <Header />
        <Container sx={{ mt: 4 }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/event/:slug" element={<Event />} />
            <Route path="/admin" element={<AdminLogin />} />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}

export default App;
