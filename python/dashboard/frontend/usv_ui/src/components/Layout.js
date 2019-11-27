import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import '../App.css';

// Router
import { Link } from 'react-router-dom';

// Material-ui element imports below //

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

// Home icon
import HomeIcon from '@material-ui/icons/Home';

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
    textDecorationStyle: 'none'
  },

  listText: {
    margin: 20
  },
}));


export default function Layout() {
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

  const home = side => {
    return (
      <div
        className={classes.list}
        role="presentation"
        onClick={toggleDrawer(side, false)}
        onKeyDown={toggleDrawer(side, false)}
      >
        <Link to={"/"}>
          <List>
            {/* Home button */}
            <ListItem button key={"home"}>
              <ListItemIcon>
                <HomeIcon />
              </ListItemIcon>
              <ListItemText primary={"Home"} />
            </ListItem>
          </List>
        </Link>
      </div>
    );
  }

  const controlList = side => {
    return (
      <div
        className={classes.list}
        role="presentation"
        onClick={toggleDrawer(side, false)}
        onKeyDown={toggleDrawer(side, false)}
      >
        <List>
          <Link to={"/remote-control"}>
            {/* RC Mode Button */}
            <ListItem button key={"rc_mode"}>
              <ListItemIcon>
                <SportsEsportsIcon />
              </ListItemIcon>
              <ListItemText primary={"Remote Control Mode"} />
            </ListItem>
          </Link>

          {/* Autonomous Mode Button */}
          <Link to={"/autonomous"}>
            <ListItem button key={"auto_mode"}>
              <ListItemIcon>
                <DesktopWindowsIcon />
              </ListItemIcon>
              <ListItemText primary={"Autonomous Control Mode"} />
            </ListItem>
          </Link>

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
          <Link to={"/tuning"}>
            <ListItem button key={"pid_settings"}>
              <ListItemIcon>
                <TuneIcon />
              </ListItemIcon>
              <ListItemText primary={"PID Tuning Parameters"} />
            </ListItem>
          </Link>

          <Link to={"/settings"}>
            <ListItem button key={"general_settings"}>
              <ListItemIcon>
                <SettingsIcon />
              </ListItemIcon>
              <ListItemText primary={"Settings"} />
            </ListItem>
          </Link>

          <Link to={"/about"}>
            <ListItem button key={"about"}>
              <ListItemIcon>
                <SettingsIcon />
              </ListItemIcon>
              <ListItemText primary={"About"} />
            </ListItem>
          </Link>

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

            {/* 
              Laying out drawer.
              home, controlList, and settingsList are generated here.
            */}
            <SwipeableDrawer
              open={state.left}
              onClose={toggleDrawer("left", false)}
              onOpen={toggleDrawer("left", true)}
            >
              <Typography variant='h5' className={classes.listText}>
                USV Home Page
                <Divider />
                {home("left")}
              </Typography>

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
