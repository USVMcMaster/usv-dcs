import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
// Router
import { Link } from 'react-router-dom';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    padding: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(4),    
  },

  text: {
    textAlign: "center"
  },

  button: {
    padding: theme.spacing(20),
    // margin: theme.spacing(10),
    width: 165
  },
}));

export default function Home() {
  const classes = useStyles();

  return (
    <div>

      <Paper className={classes.paper}>
        <Typography className={classes.text} variant="h5">
          Welcome to the USV Dashboard Home Page!
      </Typography>

        <Typography className={classes.text} variant="h5">
          Please select a control method to proceed.
      </Typography>
      </Paper>

      <Grid container className={classes.root}>
        <Grid container justify={"space-around"} alignItems={"center"} className={classes.buttonContainer}>

          <Link to={"/remote-control"}>
            <Button variant="outlined" size="large" color="primary" className={classes.button}>
              Remote Control Mode
            </Button>
          </Link>

          <Link to={"/autonomous"}>
            <Button variant="outlined" size="large" color="primary" className={classes.button}>
              Autonomous Control Mode
            </Button>
          </Link>
        </Grid>
      </Grid>

    </div>
  );
}
