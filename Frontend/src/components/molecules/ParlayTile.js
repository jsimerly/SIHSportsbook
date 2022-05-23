import React, { Component, useEffect, useState } from "react";
import { 
    Grid,
    Box,
    InputAdornment,
    FormControl,
    InputLabel,
    OutlinedInput,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

import ParlayBet from "../atoms/parlayBet";

export default function ParlayTile(props){
    const selectedBets = props.selectedBets
    const [wager, setWager] = useState()
    const [toWin, setToWin] = useState()
    const line = 0

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

    function handleRemoveBet() {
        props.handleRemoveBet(props.bet)
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

    const parlayLine = calculateParlayLine()

    function getVanityParlayLine(){
        if (parlayLine > 0) {
            return "+" + parlayLine
        } else {
            return parlayLine
        }
    }

    const re = /^[0-9]\d*(?:\.\d{0,2})?$/;

    function handleWager(e) {
        if (e.target.value==='' || re.test(e.target.value)) {
            setWager(e.target.value)
            
            let winAmount = 0

            if (parlayLine > 0) {
               winAmount = parlayLine/100 * e.target.value
            } else {
                winAmount = 100/(-1*parlayLine) * e.target.value
            }

            winAmount = parseFloat(winAmount).toFixed(2)
            setToWin(winAmount)
        }
    }

    function handleToWin(e){
        if (e.target.value==='' || re.test(e.target.value)) {
            setToWin(e.target.value)
        }

            let betAmount = 0

            if (line > 0) {
               betAmount = (e.target.value * 100)/parlayLine
            } else {
                betAmount = (e.target.value * parlayLine * -1)/100
            }

            betAmount = parseFloat(betAmount).toFixed(2)
            setWager(betAmount)
    } 


    function parlayBody() {
        return (
            <Box sx={{border:1, p:1}}>
                <Grid container sx={{pr:1 , pl: 1}}>
                    <Grid item xs={6}>
                        {props.selectedBets.length}-Leg Parlay
                    </Grid>
                    <Grid container justifyContent={"flex-end"} item xs={6}>
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
                        <Grid item xs={5} sx={{mr:1, mb:2}}>
                            <FormControl>
                                <InputLabel htmlFor="outlined-adornment-wager">Wager</InputLabel>
                                <OutlinedInput
                                    size="small"
                                    inputMode="numberic"
                                    id="outlined-adornment-wager"
                                    value={wager}
                                    onChange={handleWager}
                                    startAdornment={<InputAdornment position="start">$</InputAdornment>}
                                    label="wager"
                                />
                            </FormControl>
                        </Grid>
                        <Grid item xs={5} sx={{ml:1, mb:2}}>
                            <FormControl>
                                <InputLabel htmlFor="outlined-adornment-to-win">To Win</InputLabel>
                                <OutlinedInput
                                    size="small"
                                    inputMode="numberic"
                                    id="outlined-adornment-to-win"
                                    value={toWin}
                                    onChange={handleToWin}
                                    startAdornment={<InputAdornment position="start">$</InputAdornment>}
                                    label="toWin"
                                />
                            </FormControl>
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