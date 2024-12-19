import React from 'react';
import { Button, Card, CardContent, Typography } from '@mui/material';

const TrainingModule = () => (
  <div style={{ padding: '20px' }}>
    <h2>Training Module</h2>
    <Card>
      <CardContent>
        <Typography variant="h5">Module 1: React Basics</Typography>
        <Typography variant="body2">
          Learn the fundamentals of React, including components, state, and props.
        </Typography>
        <Button variant="contained" color="primary" style={{ marginTop: '10px' }}>
          Start Module
        </Button>
      </CardContent>
    </Card>
  </div>
);

export default TrainingModule;
