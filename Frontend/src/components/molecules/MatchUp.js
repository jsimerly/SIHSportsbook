import React, { Component } from "react";
import { 
    Grid,
    Box,
    ToggleButtonGroup,
    Typography,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){
    const data = props.data.data
    const id = props.betId

    return (
    <Box sx={{margin:1}}>
        <Grid container columns={20}>
            <Grid item md={8} sx={{border:1}}>
                {data.team1}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betData={data.sp_pos} betId={id}/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betData={data.over} betId={id} type="over"/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betData={data.ml_pos} betId={id} type="pos"/>
            </Grid>
        </Grid>
        <Grid container columns={20}>
            <Grid item md={8} sx={{border:1}}>
                {data.team2}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betData={data.sp_neg} betId={id}/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betData={data.under} betId={id} type="under"/>
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile betData={data.ml_neg} betId={id}/>
            </Grid>
        </Grid>
    </Box>
    )
}