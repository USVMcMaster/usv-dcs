import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

// Main Body
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip'

// Snacks
import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';

const useStyles = makeStyles(theme => ({
  // root == container level
  root: {
    flexGrow: 1,
    padding: 20,
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

export default function ConsecutiveSnackbars() {
  const queueRef = React.useRef([]);
  const [open, setOpen] = React.useState(false);
  const [messageInfo, setMessageInfo] = React.useState(undefined);

  const processQueue = () => {
    if (queueRef.current.length > 0) {
      setMessageInfo(queueRef.current.shift());
      setOpen(true);
    }
  };

  // eslint-disable-next-line
  const handleClick = message => () => {
    queueRef.current.push({
      message,
      key: new Date().getTime(),
    });

    if (open) {
      // immediately begin dismissing current message
      // to start showing new one
      setOpen(false);
    } else {
      processQueue();
    }
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
  };

  const handleExited = () => {
    processQueue();
  };

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
              // onClick={handleClick('Test3')}
              className={classes.button}>Generate Path
           </Button>
          </Tooltip>

          <Tooltip title="Click this button to remove all markers" placement="bottom">
            <Button
              id="btn_reset"
              variant="outlined"
              color="primary"
              // onClick={handleClick('Test4')}
              className={classes.button}>Reset
            </Button>
          </Tooltip>

        </Grid>
      </Grid>

      <Grid item xs>
        <Paper className={classes.mapPaper}>
          <div id="map"></div>
        </Paper>
      </Grid>

      {/* Snackbar handler */}
      <Snackbar
        key={messageInfo ? messageInfo.key : undefined}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'left',
        }}
        open={open}
        autoHideDuration={6000}
        onClose={handleClose}
        onExited={handleExited}
        ContentProps={{
          'aria-describedby': 'message-id',
        }}
        message={<span id="message-id">{messageInfo ? messageInfo.message : undefined}</span>}
        action={[
          <Button key="undo" color="secondary" size="small" onClick={handleClose}>
            UNDO
          </Button>,
          <IconButton
            key="close"
            aria-label="close"
            color="inherit"
            className={classes.close}
            onClick={handleClose}
          >
            <CloseIcon />
          </IconButton>,
        ]}
      />
    </div>
  );
}
