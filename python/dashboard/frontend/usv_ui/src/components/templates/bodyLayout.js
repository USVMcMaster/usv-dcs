import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

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
        margin: 20
      },

      paper: {
        padding: theme.spacing(2),
        height: 400,
        width: 350
      },
  }));

export default function PaperSheet() {
    const classes = useStyles();
    
    return (
        <Grid container className={classes.root}>
            <Grid item className={classes.itembox}>
                <Paper className={classes.paper}>
                    <div id="map"></div>
                </Paper>
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