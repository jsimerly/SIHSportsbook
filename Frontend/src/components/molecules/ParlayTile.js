import React, { Component, useEffect, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

import ParlayBet from "../atoms/parlayBet";


export default function ParlayTile(props){
    const selectedBets = props.selectedBets

    useEffect(() => {
        checkForBets()
    },[props.selectedBets]);

    function checkForBets() {
        if (props.selectedBets.length === 0) {
            return (<div></div>)
        } else {
            return (<div> {parlayBody()} </div>)
        }
    }

    function getParlayLines(){
        let parlayLines = []
        selectedBets.map((bet, index) => {
            parlayLines.push(bet.betData.line)
        })
        return parlayLines
    }

    const betLines = getParlayLines()

    function calculateParlayLine() {
        const decimalOdds = []

        betLines.map((line, index) => {
            if (line < 0) {
                decimalOdds.push(1-(100/line))
            } else {
                decimalOdds.push((line/100)+1)
            }    
        })

        if (decimalOdds.length === 0){
            return 0
        } else {
            var parlayOdds = decimalOdds.reduce(function(a,b) {
                return a * b;
            });

            if (parlayOdds > 2.00) {
                return Math.round((parlayOdds-1)*100)
            } else {
                return Math.round((-100) / (parlayOdds-1))
            }
        }

    }
    //Need to fix empty array for betting lines
    const parlayLine = calculateParlayLine()

    function getVanityParlayLine(){
        if (parlayLine > 0) {
            return "+" + parlayLine
        } else {
            return parlayLine
        }
    }


    function parlayBody() {
        return (
            <Box sx={{border:1, p:1}}>
                <Grid container sx={{mr:1 , ml: 1}}>
                    <Grid item xs={6}>
                        {props.selectedBets.length}-Leg Parlay
                    </Grid>
                    <Grid container justifyContent={"flex-end"} item xs={5}>
                        {getVanityParlayLine()}
                    </Grid>
                </Grid>
                <Box sx={{mb:1}}>
                    {props.selectedBets.map((bet, index) => {
                        return (
                            <ParlayBet
                                bet={bet}
                                handleRemoveBet={props.handleRemoveBet}
                            />
                        )
                    })}
                </Box>
                <Box>
                    <Grid container justifyContent={"center"}>
                        <Grid item xs={4} sx={{mr:1, mb:2}}>
                            <TextField size="small" label="WAGER"/>
                        </Grid>
                        <Grid item xs={4} sx={{ml:1, mb:2}}>
                            <TextField size="small" label="TO WIN"/>
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