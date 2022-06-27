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

export default function NewLeaguePage(props){

    return (
        <Box sx={{mt:5}}>
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component='h5' variant='h5'>
                        Create League
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl sx={{minWidth: '40%'}}>
                        <InputLabel> Sleeper Id </InputLabel>
                        <Input
                            name="email"
                            type="email"
                            autoComplete="email"
                            
                        />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography component='h5' variant='h5'>
                        Find a League
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl sx={{minWidth: '40%'}}>
                        <InputLabel> Search League Name </InputLabel>
                            <Input
                                name="password"
                                type="password"
                                autoComplete="password"
                            
                            />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="primary"
                    >
                        Search
                    </Button>
                </Grid>
            </Grid>
        </Box>
    )
}