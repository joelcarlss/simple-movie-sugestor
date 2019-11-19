import React, { useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Switch from '@material-ui/core/Switch';
import { useAppState } from '../useAppState'


const useStyles = makeStyles(theme => ({
    formControl: {
        margin: theme.spacing(1),
        minWidth: 120
    }
}));


export default function SimpleSelect() {
    const { users, name, setName, amount, setAmount, algoritm, setAlgoritm, updateResult, showUser, setShowUser } = useAppState()
    const classes = useStyles();

    useEffect(() => {
        userList(users)
    }, []);

    const handleChange = event => {
        setName(event.target.value);
        updateResult(showUser, event.target.value, amount, algoritm)
    };
    const changeAlgoritm = event => {
        setAlgoritm(event.target.value)
        updateResult(showUser, name, amount, event.target.value)
    };
    const toggle = () => {
        setShowUser(!showUser)
        updateResult(showUser, name, amount, algoritm)
    }

    const handleAmountChange = event => {
        const re = /^[0-9\b]+$/;
        if (event.target.value === '' || re.test(event.target.value)) {
            setAmount(event.target.value);
            updateResult(showUser, name, event.target.value, algoritm)
        }
    }



    const userList = (users) => {
        if (users) {
            return users.map(user => (<MenuItem key={user.userId} value={user.userId}>{user.name}</MenuItem>))
        }
    }


    return (
        <div>
            <FormControl>
                <Switch
                    checked={showUser}
                    onChange={() => toggle()}
                    value="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                />
            </FormControl>
            <FormControl className={classes.formControl}>
                <InputLabel >User</InputLabel>
                <Select

                    id="demo-simple-select"
                    value={name}
                    onChange={handleChange}
                >
                    {userList(users)}
                </Select>
            </FormControl>
            <FormControl className={classes.formControl}>
                <TextField
                    label="Amount of results"
                    value={amount}
                    onChange={handleAmountChange}
                    id="formatted-numberformat-input"
                />
            </FormControl>
            <FormControl className={classes.formControl}>
                <InputLabel >Algoritm</InputLabel>
                <Select

                    id="simple-select"
                    value={algoritm}
                    onChange={changeAlgoritm}
                >
                    <MenuItem value={"euclidean"}>Euclidean</MenuItem>
                    <MenuItem value={"pearson"}>Pearson</MenuItem>
                </Select>
            </FormControl>
        </div>
    );
}
