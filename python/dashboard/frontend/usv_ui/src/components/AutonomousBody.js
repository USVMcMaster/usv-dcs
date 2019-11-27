import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

// Main Body
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip'
import GetMapData from './GetMapData';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    padding: theme.spacing(4),
  },

  mapPaper: {
    padding: theme.spacing(2),
    height: 500,
  },

  button: {
    padding: theme.spacing(2),
    marginBottom: theme.spacing(2),
    width: 165
  },

  // Tooltip
  absolute: {
    position: 'absolute',
    bottom: theme.spacing(2),
    right: theme.spacing(3),
  },

  // Snack
  close: {
    padding: theme.spacing(0.5),
  },
}));

export default function AutonomousBody() {

  const classes = useStyles();
  return (
    <div>
      <Grid container className={classes.root}>
        <Grid container justify={"space-around"} alignItems={"center"} className={classes.buttonContainer}>
          <Tooltip title="Click on the map after clicking this button to set the start point" placement="bottom">
            <Button
              id="btn_start"
              variant="outlined"
              color="primary"
              // onClick={handleClick('Click on the map to register the start point')}
              className={classes.button}>Set Start Point
            </Button>
          </Tooltip>

          <Tooltip title="Click on the map after clicking this button to set the end point" placement="bottom">
            <Button
              id="btn_end"
              variant="outlined"
              color="primary"
              // onClick={handleClick('Click on the map to register the end point')}
              className={classes.button}>Set End Point
           </Button>
          </Tooltip>

          <Tooltip title="Click this button to generate a path between the start and end point" placement="bottom">
            <Button
              id="btn_generate"
              variant="outlined"
              color="primary"
              // onClick={gen_map_snapshot}
              // value={[12,13,14]}
              className={classes.button}>Generate Path
           </Button>
          </Tooltip>

          <Tooltip title="Click this button to remove all markers" placement="bottom">
            <Button
              id="btn_reset"
              variant="outlined"
              color="primary"
              // onClick={handleClick('Removed all markers')}
              className={classes.button}>Reset
            </Button>
          </Tooltip>

        </Grid>
      </Grid>

      {/* <Grid item xs={12} sm={6} xl={6}> */}
      <Grid container>
        <Grid item xs={12} xl={6} className={classes.gridItem}>
          <Paper className={classes.mapPaper}>
            <div id="map"></div>
            Map Here
        </Paper>
        </Grid>

        <Grid item xs={12} xl={6} className={classes.gridItem}>
          <Paper className={classes.mapPaper}>
            <GetMapData />
        </Paper>
        </Grid>
      </Grid>
    </div>
  );
}