import React from 'react';
import Table from './components/DenseTable'
import SimpleSelect from './components/SimpleSelect'
import { Provider } from './useAppState'
import './App.css';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <CssBaseline />
          <Container maxWidth="sm">
            <Typography component="div" style={{ height: '60vh' }} >
              <SimpleSelect />
              <Table />
            </Typography>
          </Container>
        </div>
      </header>
    </div>
  );
}

export default () => <Provider><App /></Provider>
