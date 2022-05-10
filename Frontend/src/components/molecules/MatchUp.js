import React, { Component } from "react";
import { 
    Grid,
    Box,
    ToggleButtonGroup,
    Typography,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){

    return (
    <Box sx={{margin:1}}>
        <Grid container columns={20}>
            <Grid item md={8} sx={{border:1}}>
                Team 1
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betValue="+3.5"/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betValue="O 200"/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betValue="+220"/>
            </Grid>
        </Grid>
        <Grid container columns={20}>
            <Grid item md={8} sx={{border:1}}>
                test 1
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betValue="-3.5"/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betValue="U 200"/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betValue="-180"/>
            </Grid>
        </Grid>
    </Box>
    )
}