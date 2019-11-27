import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

// Top bar
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';

// Top bar title
import Typography from '@material-ui/core/Typography';

// Top bar menu button
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

// SwipeableDrawer
import SwipeableDrawer from '@material-ui/core/SwipeableDrawer';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import Divider from '@material-ui/core/Divider';

// Icons for control modes
import SportsEsportsIcon from '@material-ui/icons/SportsEsports';
import DesktopWindowsIcon from '@material-ui/icons/DesktopWindows';

// Icons for settings
import SettingsIcon from '@material-ui/icons/Settings';
import TuneIcon from '@material-ui/icons/Tune';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    width: "100%"
  },

  title: {
    flexGrow: 1,
    textAlign: "center"
  },

  menuButton: {
    // marginRight: theme.spacing(2),
  },

  listText: {
    margin: 20
  },
}));


export default function HeaderManager() {
  const classes = useStyles();

  // Drawer variables and functions
  const [state, setState] = React.useState({
    top: false,
    left: false,
    bottom: false,
    right: false,
  });

  const toggleDrawer = (side, open) => event => {
    
    // Allow tab and shift tab within drawer
    if (event && event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
      return;
    }

    setState({ ...state, [side]: open });
  };

  const controlList = side => {
    return (
      <div
        className={classes.list}
        role="presentation"
        onClick={toggleDrawer(side, false)}
        onKeyDown={toggleDrawer(side, false)}
      >

        <List>
          {/* RC Mode Button */}
          <ListItem button key={"rc_mode"}>
            <ListItemIcon>
              <SportsEsportsIcon />
            </ListItemIcon>
            <ListItemText primary={"Remote Control Mode"} />
          </ListItem>

          {/* Autonomous Mode Button */}
          <ListItem button key={"auto_mode"}>
            <ListItemIcon>
              <DesktopWindowsIcon />
            </ListItemIcon>
            <ListItemText primary={"Autonomous Control Mode"} />
          </ListItem>

        </List>
      </div>
    )
  };

  const settingsList = side => {
    return (
      <div
        className={classes.list}
        role="presentation"
        onClick={toggleDrawer(side, false)}
        onKeyDown={toggleDrawer(side, false)}
      >
        <List>

          <ListItem button key={"general_settings"}>
            <ListItemIcon>
              <SettingsIcon />
            </ListItemIcon>
            <ListItemText primary={"Settings"} />
          </ListItem>
          
          <ListItem button key={"pid_settings"}>
            <ListItemIcon>
              <TuneIcon />
            </ListItemIcon>
            <ListItemText primary={"PID Tuning Parameters"} />
          </ListItem>

        </List>
      </div>
    )
  };

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <div>
            <IconButton
              edge="start"
              className={classes.menuButton}
              color="inherit"
              aria-label="menu"
              onClick={toggleDrawer("left", true)}
            >
              <MenuIcon />
            </IconButton>


            <SwipeableDrawer
              open={state.left}
              onClose={toggleDrawer("left", false)}
              onOpen={toggleDrawer("left", true)}
            >
              <Typography variant='h5' className={classes.listText}>
                Control Modes
                <Divider />
                {controlList("left")}
              </Typography>

              <Typography variant='h5' className={classes.listText}>
                Settings
                <Divider />
                {settingsList("left")}
              </Typography>

            </SwipeableDrawer>
          </div>

          <Typography variant="h6" className={classes.title}>
            Unmanned Surface Vehicle Dashboard
          </Typography>

        </Toolbar>
      </AppBar>
    </div>
  );
}


