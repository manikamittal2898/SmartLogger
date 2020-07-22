import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Chip from '@material-ui/core/Chip';

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
    maxWidth: 300,
  },
  chips: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  chip: {
    margin: 2,
  },
  noLabel: {
    marginTop: theme.spacing(3),
  },
}));

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

const names = [
  'IPSDashboard-UX',
  'support-ode-ux',
  'Documents-UX',
  'Advisories-UX',
  'guidedPath-ux-prod',
  'OrderStatusUX',
  'KbArticle-UX',
  'article-ux',
  'flatcontents-ux',
  'ProductSupport-UX',
  'security-portal-ux',
  'masthead-ux',
  'support-home-ux',
  'drivers-ux',
  'sonar-validator-ux',
];

function getStyles(name, appName, theme) {
  return {
    fontWeight:
      appName.indexOf(name) === -1
        ? theme.typography.fontWeightRegular
        : theme.typography.fontWeightMedium,
  };
}

export default function MultipleSelect() {
  const classes = useStyles();
  const theme = useTheme();
  const [appName, setAppName] = React.useState([]);

  const handleChange = (event) => {
    setAppName(event.target.value);
  };

 /* const handleChangeMultiple = (event) => {
    const { options } = event.target;
    const value = [];
    for (let i = 0, l = options.length; i < l; i += 1) {
      if (options[i].selected) {
        value.push(options[i].value);
      }
    }
    setPersonName(value);
  };*/

  return (
    <div>
     
      
      <FormControl className={classes.formControl}>
        <InputLabel id="demo-mutiple-chip-label">Add Filters+</InputLabel>
        <Select
          labelId="demo-mutiple-chip-label"
          id="demo-mutiple-chip"
          multiple
          value={appName}
          onChange={handleChange}
          input={<Input id="select-multiple-chip" />}
          renderValue={(selected) => (
            <div className={classes.chips}>
              {selected.map((value) => (
                <Chip key={value} label={value} className={classes.chip} />
              ))}
            </div>
          )}
          MenuProps={MenuProps}
        >
          {names.map((name) => (
            <MenuItem key={name} value={name} style={getStyles(name, appName, theme)}>
              {name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
     
    </div>
  );
}