import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
// import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles(theme => ({
  // root == container level
  root: {
    flexGrow: 1,
    padding: 20,
    // height,
    // marginTop:20


  },
  // control == item level
  itembox: {
    // height: 100,
    // width: 100,
    // margin: 50
  },

  mapPaper: {
    padding: theme.spacing(2),
    height: 500,
    // width: "100%"
  },

  buttonContainer: {

  },

  button: {
    padding: theme.spacing(2),
    // margin: 10,
    marginBottom: theme.spacing(2),
    width: 165
  },
}));

export default function PaperSheet() {
  const classes = useStyles();

  return (

    <Grid container className={classes.root}>
      <Grid container justify={"space-around"} alignItems={"center"} className={classes.buttonContainer}>
          <Button variant="outlined" color="primary" className={classes.button}>Set Start Point</Button>
          <Button variant="outlined" color="primary" className={classes.button}>Set End Point</Button>
          <Button variant="outlined" color="primary" className={classes.button}>Reset</Button>
        </Grid>
        
        <Grid item xs>
          <Paper className={classes.mapPaper}>
            <div id="map"></div>
          </Paper>
        </Grid>
    </Grid>
  )
}