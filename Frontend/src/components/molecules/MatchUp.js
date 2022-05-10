import React, { Component } from "react";
import { 
    Grid,
    Box,
    ToggleButtonGroup,
    Typography,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){
    const matchups = 
    (<Box>
        <Grid container spacing={0} gap={0}>
            <Grid item md={4}>
                test 1
            </Grid>
            <Grid item>
                test 2
            </Grid>
        </Grid>
    </Box>)
    return (<Box>{matchups}</Box>)
}