import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

export default function ParlayBet(props){ 
    function handleRemoveBet() {
        props.handleRemoveBet(props.bet)
    }

    return (
        <Box>
            <Grid container sx={{border:1, p:1}}>
                <Grid item xs={1}>
                    <IconButton onClick={handleRemoveBet}>
                        <RemoveCircleOutlineIcon sx={{fontSize: 10}}/>
                    </IconButton>
                </Grid>
                <Grid item>
                    <Box>
                        {props.bet.vanity.main}
                    </Box>
                    <Box>
                        {props.bet.vanity.secondary}
                        
                    </Box>
                    <Box>
                        {props.bet.vanity.teams}
                    </Box>
                </Grid>
            </Grid>
        </Box>
    )
}