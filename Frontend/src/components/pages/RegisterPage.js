import React, { useState, useEffect } from  "react";
import {
    useNavigate,
} from "react-router-dom";
import { 
    Button, 
    Grid, 
    Typography, 
    FormControl,
    Input,
    InputLabel,
    Box
 } from '@mui/material';

 export default function RegisterPage(props){
     const [email, setEmail] = useState()
     const [password1, setPassword1] = useState()
     const [password2, setPassword2] = useState()
     const [error, setError] = useState()
     const navigate = useNavigate()

    function handleEmailChanged(e) {
        setEmail(e.target.value)
    }

    function handlePasswordOneChanged(e){
        setPassword1(e.target.value)
    }

    function handlePasswordTwoChanged(e){
        setPassword2(e.target.value)
    }

    function postToRegister(){
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password1,
            })
        }

        fetch('/api/account/create-user/', requestOptions)
        .then((response) => {
            if (response.status===201) {
                navigate('/login')
            } else {
                setError(response.json())
            }
        })
    }

    function handleRegister(){
        if (password1 !== password2) {
            alert('passwords do not match!')
        } else {
            postToRegister()
        }
    }


    return (
        <Box sx={{mt:5}}>
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component='h4' variant='h4'>
                        Register
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <InputLabel> e-mail </InputLabel>
                        <Input
                            name="email"
                            type="email"
                            autoComplete="email"
                            onChange={handleEmailChanged}
                        />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <InputLabel> password </InputLabel>
                            <Input
                                name="password"
                                type="password"
                                autoComplete="password"
                                onChange={handlePasswordOneChanged}
                            />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <InputLabel> re-enter password </InputLabel>
                            <Input
                                name="password"
                                type="password"
                                autoComplete="password"
                                onChange={handlePasswordTwoChanged}
                            />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleRegister}
                    >
                        Register
                    </Button>
                </Grid>
            </Grid>
        </Box>
    )
 }