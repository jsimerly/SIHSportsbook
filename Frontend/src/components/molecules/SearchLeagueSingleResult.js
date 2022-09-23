import React, { Component, useState, useEffect } from "react";
import {
    Grid,
    Box,
    IconButton,
    Typography,
    List,
    ListItem,
    Button,
 } from '@mui/material';

 import CreateLeagueButton from "../atoms/CreateLeagueButton";
 import JoinLeagueButton from "../atoms/JoinLeagueButton";

export default function SearchLeagueSingleResult(props){

    return (
            <Box sx={{
                flexDirection: 'column',
                borderRadius: 1,
                border: 1,
                width: '100%'
                }}
                
            >
            <Grid container>
                <Grid item xs={9}>
                    <Box 
                        display='flex' 
                        justifyContent={'flex-start'}  
                        >
                            {props.league_label}
                    </Box>
                </Grid>
                <Grid item xs={3}>
                    <JoinLeagueButton
                        league_id = {props.league_id}
                        getCookie = {props.getCookie}
                    />
                </Grid>
            </Grid>
                
            </Box>
    )
}