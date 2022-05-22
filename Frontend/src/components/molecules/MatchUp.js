import React, { Component } from "react";
import { 
    Grid,
    Box,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){
    const data =  props.matchupData.data

    function BetTileTemplate(betType, betData, team){
        return (
            <BetTile
                betType={betType}
                data={betData}
                team={team}

                matchupData={props.matchupData}
                betSelectedHandler={props.betSelectedHandler}
                selectedBets={props.selectedBets}
                checkDupsIndex={props.checkDupsIndex}
                vig={props.vig}
            />
        )
    }

    return (
    <Box sx={{margin:1}}>
        <Grid container columns={20}>
            <Grid item md={8}  sx={{p:1, border:1, display: "flex", alignItems: "center" }}>
                {data.team1}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("sp_pos", data.sp_pos, data.team1)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("over", data.over, data.team1)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("ml_pos", data.ml_pos, data.team1)}
            </Grid>
        </Grid>
        <Grid container columns={20}>
            <Grid item md={8} sx={{p:1, border:1, display: "flex", alignItems: "center" }}>
                {data.team2}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("sp_neg", data.sp_neg, data.team2)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("under", data.under, data.team2)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("ml_neg", data.ml_neg, data.team2)}
            </Grid>
        </Grid>
    </Box>
    )
}