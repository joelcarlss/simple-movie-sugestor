import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { useAppState } from '../useAppState'

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
  },
  paper: {
    marginTop: theme.spacing(3),
    width: '100%',
    overflowX: 'auto',
    marginBottom: theme.spacing(2),
  },
}));


export default function DenseTable() {
  const classes = useStyles();
  const { result, showUser, userResult } = useAppState()

  const showNames = (showUser) => {
    if (showUser) {
      return (
        <>
          <TableCell>Title</TableCell>
          <TableCell align="right">Year</TableCell>
          <TableCell align="right">Weighted Score</TableCell>
        </>
      )
    } else {
      return (
        <>
          <TableCell>Name</TableCell>
          <TableCell align="right">Weighted Score</TableCell>
        </>
      )
    }
  }

  const showRes = (result, showUser) => {
    console.log(result)
    if (showUser) {
      return result.map(res => (
        <TableRow key={res.id}>
          <TableCell component="th" scope="row">
            {res.title}
          </TableCell>
          <TableCell align="right">{res.year}</TableCell>
          <TableCell align="right">{res.w_score}</TableCell>
        </TableRow>
      ))
    } else {
      return userResult.map(res => (
        <TableRow key={res.userId}>
          <TableCell component="th" scope="row">{res.name}</TableCell>
          <TableCell align="right">{res.w_score}</TableCell>
        </TableRow>
      ))
    }
  }

  return (
    <div className={classes.root}>
      <Paper className={classes.paper}>
        <Table className={classes.table} size="small" aria-label="a dense table">
          <TableHead>
            <TableRow>
              {showNames(showUser)}
            </TableRow>
          </TableHead>
          <TableBody>
            {showRes(result, showUser)}
          </TableBody>
        </Table>
      </Paper>
    </div>
  );
}