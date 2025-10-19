import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Box } from '@mui/material';
import Admin from './Admin';

// In a real app, this would be a more secure authentication method.
const ADMIN_PASSWORD = process.env.REACT_APP_ADMIN_PASSWORD;

function AdminLogin() {
  const [password, setPassword] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [error, setError] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    if (password === ADMIN_PASSWORD) {
      setIsAuthenticated(true);
      setError('');
    } else {
      setError('Incorrect password');
    }
  };

  if (isAuthenticated) {
    return <Admin />;
  }

  return (
    <Container maxWidth="xs">
      <Box sx={{ mt: 8, textAlign: 'center' }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Admin Login
        </Typography>
        <form onSubmit={handleLogin}>
          <TextField
            label="Password"
            type="password"
            variant="outlined"
            fullWidth
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            error={!!error}
            helperText={error}
          />
          <Button type="submit" variant="contained" color="primary" fullWidth>
            Login
          </Button>
        </form>
      </Box>
    </Container>
  );
}

export default AdminLogin;
