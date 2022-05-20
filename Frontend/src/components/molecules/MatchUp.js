import React, { Component } from "react";
import { 
    Grid,
    Box,
} from "@mui/material";
import BetTile from "../atoms/BetTile"

export default function MatchUp(props){
    const data =  props.matchupData.data

    return (
    <Box sx={{margin:1}}>
        <Grid container columns={20}>
            <Grid item md={8}  sx={{p:1, border:1, display: "flex", alignItems: "center" }}>
                {data.team1}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="sp_pos" 
                    data={data.sp_pos}
                    team={data.team1} 
                    matchupData={props.matchupData}

                    betSelectedHandler={props.betSelectedHandler}
                    selectedBets={props.selectedBets}
                    checkDupsIndex={props.checkDupsIndex}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="over" 
                    data={data.over} 
                    team={data.team1}
                    matchupData={props.matchupData}

                    betSelectedHandler={props.betSelectedHandler}
                    selectedBets={props.selectedBets}
                    checkDupsIndex={props.checkDupsIndex}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="ml_pos" 
                    data={data.ml_pos} 
                    team={data.team1}
                    matchupData={props.matchupData}

                    betSelectedHandler={props.betSelectedHandler}
                    selectedBets={props.selectedBets} 
                    checkDupsIndex={props.checkDupsIndex}
                />
            </Grid>
        </Grid>
        <Grid container columns={20}>
            <Grid item md={8} sx={{p:1, border:1, display: "flex", alignItems: "center" }}>
                {data.team2}
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="sp_neg" 
                    data={data.sp_neg}
                    team={data.team2}
                    matchupData={props.matchupData}

                    betSelectedHandler={props.betSelectedHandler}
                    selectedBets={props.selectedBets}
                    checkDupsIndex={props.checkDupsIndex}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="under" 
                    data={data.under} 
                    team={data.team2}
                    matchupData={props.matchupData}

                    betSelectedHandler={props.betSelectedHandler}
                    selectedBets={props.selectedBets}
                    checkDupsIndex={props.checkDupsIndex}
                />
            </Grid>
            <Grid item md={4} sx={{border:1}}>
                <BetTile 
                    betType="ml_neg" 
                    data={data.ml_neg}
                    team={data.team2} 
                    matchupData={props.matchupData}

                    checkDupsIndex={props.checkDupsIndex}
                    betSelectedHandler={props.betSelectedHandler}
                    selectedBets={props.selectedBets}
                />
            </Grid>
        </Grid>
    </Box>
    )
}