import React, { Component } from "react";
import { 
    Grid,
    Box,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){
    const id = props.matchupData.id
    const data =  props.matchupData.data

    function handleBetButtonSelected(betType) {
        props.betHandler(id, betType)
    }

    return (
    <Box sx={{margin:1}}>
        <Grid container columns={20}>
            <Grid item md={8}  sx={{border:1, display: "flex", alignItems: "center" }}>
                {data.team1}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="sp_pos" 
                    data={data.sp_pos} 
                    betHandler={handleBetButtonSelected}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="over" 
                    data={data.over} 
                    betHandler={handleBetButtonSelected}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="ml_pos" 
                    data={data.ml_pos} 
                    betHandler={handleBetButtonSelected} 
                />
            </Grid>
        </Grid>
        <Grid container columns={20}>
            <Grid item md={8} sx={{border:1, display: "flex", alignItems: "center" }}>
                {data.team2}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="sp_neg" 
                    data={data.sp_neg}
                    betHandler={handleBetButtonSelected}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="under" 
                    data={data.under} 
                    betHandler={handleBetButtonSelected}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="ml_neg" 
                    data={data.ml_neg} 
                    betHandler={handleBetButtonSelected}
                />
            </Grid>
        </Grid>
    </Box>
    )
}