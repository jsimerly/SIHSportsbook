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
import { impliedOddsToAmerican, getParlayOdds } from "../../util/oddHandler";

export default function ParlayTile(props){
    const selectedBets = props.selectedBets
    function cleanWager(wager){
        if (wager == 0){
            return ''
        }
        return wager
    }

    const betLines = getParlayLines()

    function calculateParlayLine() {
        const betOdds = getParlayOdds(selectedBets, props.parlayVig)
        return impliedOddsToAmerican(betOdds)
    }

    const parlayLine = calculateParlayLine()

    const [wager, setWager] = useState(cleanWager(props.parlayWager))
    const [toWin, setToWin] = useState(cleanWager(calculateToWin(props.parlayWager)))  
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
            parlayLines.push(bet.vanity.line)
        })
        return parlayLines
    }

    

    function getVanityParlayLine(){
        if (parlayLine > 0) {
            return "+" + parlayLine
        } else {
            return parlayLine
        }
    }

    const re = /^[0-9]\d*(?:\.\d{0,2})?$/;

    function calculateToWin(wager){
        let winAmount = 0
        if (parlayLine > 0) {
            winAmount = parlayLine/100 * wager
         } else {
             winAmount = 100/(-1*parlayLine) * wager
         }

         winAmount = parseFloat(winAmount).toFixed(2)
         return winAmount
    }

    function handleWager(e) {
        if (e.target.value==='' || re.test(e.target.value)) {
            setWager(e.target.value)
            props.handleWager(e.target.value)
            
            
            const winAmount = calculateToWin(e.target.value)

            setToWin(cleanWager(winAmount))
            // props.handleWager(e.target.value)
        }
    }

    function calculateWager(toWinValue){
        let betAmount = 0
        if (parlayLine > 0) {
            betAmount = (toWinValue * 100)/parlayLine
         } else {
             betAmount = (toWinValue * parlayLine * -1)/100
         }

         betAmount = parseFloat(betAmount).toFixed(2)
         return betAmount
    }

    function handleToWin(e){
        if (e.target.value==='' || re.test(e.target.value)) {
            setToWin(e.target.value)
        }

            const wager = calculateWager(e.target.value)

            setWager(cleanWager(wager))
            // props.handleWager(betAmount)
    } 


    function parlayBody() {
        return (
            <Box sx={{border:1, p:1}}>
                <Grid container sx={{pr:1 , pl: 1}}>
                    <Grid item xs={6}>
                        {props.selectedBets.length}-Leg Parlay
                    </Grid>
                    <Grid container justifyContent={"flex-end"} item xs={6}>
                        {parlayLine}
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