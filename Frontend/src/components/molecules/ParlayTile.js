import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';


export default function ParlayTile(props){
    function checkForBets() {
        if (props.selectedBets.length === 0) {
            return (<div></div>)
        } else {
            return (<div> {parlayBody()} </div>)
        }
    }

    function calcParlayLine() {
        return (-110)
    }

    function parlayBody() {
        return (
            <Box sx={{border:1}}>
                <Grid container sx={{mr:1 , ml: 1}}>
                    <Grid item xs={6}>
                        {props.selectedBets.length}-Leg Parlay
                    </Grid>
                    <Grid container justifyContent={"flex-end"} item xs={5}>
                        {calcParlayLine()}
                    </Grid>
                </Grid>
                <Box sx={{mb:1}}>
                    {props.selectedBets.map((bet, index) => {
                        return (
                            <Box>
                                <Grid container>
                                    <Grid item>
                                            Total Points
                                        </Grid>
                                    <Grid item>
                                            {bet.matchupData.data.team1} 
                                        </Grid>
                                    <Grid item>
                                            {bet.matchupData.data.team2} 
                                        </Grid>
                                    <Grid item>
                                            {bet.betData.betValue} 
                                        </Grid>
                                    </Grid>
                            </Box>
                      
                        )
                    })}
                </Box>
                <Box>
                    <Grid container justifyContent={"center"}>
                        <Grid item xs={4} sx={{mr:1, mb:2}}>
                            <TextField label="WAGER"/>
                        </Grid>
                        <Grid item xs={4} sx={{ml:1, mb:2}}>
                            <TextField label="TO WIN"/>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
         )
    }

    return (
        checkForBets()
    )
 }