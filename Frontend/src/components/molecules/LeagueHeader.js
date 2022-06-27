import React, { Component, useState } from "react";
import { Link } from 'react-router-dom';
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import AddCircleOutlineRoundedIcon from '@mui/icons-material/AddCircleOutlineRounded';

export default function LeagueHeader(props){

    return (
        <Box sx={{p:1, border:1,  }}>
            <Grid container>
                <Grid container item xs={10} sx={{alignItems: 'center',}}>
                    Leagues
                </Grid>
                <Grid item xs={2}>
                    <IconButton component={Link} to='/new-league'>
                        <AddCircleOutlineRoundedIcon/>
                    </IconButton>
                </Grid>
            </Grid>
            
        </Box>
    )
 }
