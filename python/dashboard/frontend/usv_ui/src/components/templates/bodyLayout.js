import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        padding: 20,
        // height,
        // marginTop:20
        
        
      },
    //   paper: {
    //     height: 100,
    //     width: 100,
    //   },
      control: {
        padding: theme.spacing(2),
      },
  }));

export default function PaperSheet() {
    const classes = useStyles();
    
    return (
        <Grid container className={classes.root} spacing={2}>
            <Grid item sm>
                <Paper className={classes.control}>
                    <Typography variant="h4">
                        Hopefully there will be a camera feed here someday!
                    </Typography>
                </Paper>
            </Grid>

            <Grid item sm>
                <Paper className={classes.control}>
                    <div id="map"></div>
                </Paper>
            </Grid>
        </Grid>
    )
}