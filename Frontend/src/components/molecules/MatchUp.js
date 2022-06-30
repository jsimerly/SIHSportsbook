import React, { Component } from "react";
import { 
    Grid,
    Box,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){
    const data =  props.matchupData.data

    function BetTileTemplate(betType, betData, betOdds, team){
        return (
            <BetTile
                betType={betType}
                data={betData}
                betOdds={betOdds}
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
                {BetTileTemplate("spread_team1", data.spread_team1, data.spread_team1_odds, data.team1)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("over", data.over, data.over_odds, data.team1)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("ml_team1", data.ml_team1, data.ml_team1, data.team1)}
            </Grid>
        </Grid>
        <Grid container columns={20}>
            <Grid item md={8} sx={{p:1, border:1, display: "flex", alignItems: "center" }}>
                {data.team2}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("spread_team2", data.spread_team2, data.spread_team2_odds, data.team2)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("under", data.under, data.under_odds, data.team2)}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                {BetTileTemplate("ml_team2", data.ml_team2, data.ml_team2, data.team2)}
            </Grid>
        </Grid>
    </Box>
    )
}