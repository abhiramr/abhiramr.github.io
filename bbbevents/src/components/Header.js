import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <AppBar position="static" color="transparent" elevation={0} sx={{ borderBottom: '1px solid', borderColor: 'divider' }}>
      <Toolbar>
        <Typography variant="h6" component={Link} to="/" sx={{ flexGrow: 1, color: 'primary.main', textDecoration: 'none', fontWeight: 'bold' }}>
          Broke Bibliophiles Bangalore
        </Typography>
        <Button component={Link} to="/" color="primary">Home</Button>
        <Button component={Link} to="/admin" color="primary">Admin</Button>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
