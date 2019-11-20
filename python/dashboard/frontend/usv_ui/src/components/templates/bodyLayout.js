import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
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
        // margin: 5
      },

      paper: {
        padding: theme.spacing(2),
        height: 400,
        width: 350
      },

      button: {
        padding: theme.spacing(2),
      },
  }));

export default function PaperSheet() {
    const classes = useStyles();
    
    return (
        <Grid container className={classes.root}>
            <Grid item className={classes.itembox}>
                <Paper className={classes.paper}>
                    <div id="map"></div>
                    <Button variant="contained" color="primary" className={classes.button}>Set Start Point</Button>
                    <Button variant="contained" color="primary" className={classes.button}>Set End Point</Button>
                    <Button variant="contained" color="primary" className={classes.button}>Reset</Button>
                </Paper>
                {/* <Paper>Button</Paper> */}
            </Grid>

            <Grid item className={classes.itembox}>
                <Paper className={classes.paper}>
                    <Typography variant="h4">
                        Coordinates go here!
                    </Typography>
                </Paper>
            </Grid>
        </Grid>
    )
}