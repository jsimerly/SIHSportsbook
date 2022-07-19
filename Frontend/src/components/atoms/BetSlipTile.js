import React, { Component, useEffect, useState } from "react";
import { 
    Grid,
    Box,
    IconButton,
    InputAdornment,
    FormControl,
    InputLabel,
    OutlinedInput
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

export default function BetSlipTile(props){ 
    function cleanWager(wager){
        if (wager == 0){
            return ''
        } 
        return wager
    }

    const line = props.bet.vanity.line
    const [wager, setWager] = useState(cleanWager(props.bet.betData.wager))
    const [toWin, setToWin] = useState(cleanWager(calculateWager(props.bet.betData.wager)))
    
    
    const re = /^[0-9]\d*(?:\.\d{0,2})?$/;

    function calculateToWin(wager){
        let winAmount = 0
        if (line > 0) {
            winAmount = line/100 * wager
         } else {
             winAmount = 100/(-1*line) * wager
         }

         winAmount = parseFloat(winAmount).toFixed(2)
         return winAmount
    }

    function handleWager(e) {
        if (e.target.value==='' || re.test(e.target.value)) {
            setWager(e.target.value)

            const winAmount = calculateToWin(e.target.value)
          
            setToWin(cleanWager(winAmount))
            props.handleWager(e.target.value, props.bet)
        }
    }

    function calculateWager(toWinValue){
        let betAmount = 0
        if (line > 0) {
            betAmount = (toWinValue * 100)/line
         } else {
             betAmount = (toWinValue * line * -1)/100
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
            props.handleWager(wager)
    } 

    function handleRemoveBet() {
        props.handleRemoveBet(props.bet)
    }

    return (
        <Box sx={{border:1 }}>
            <Grid container sx={{p:1, mb:1}}>
                <Grid item xs={1}>
                    <IconButton onClick={handleRemoveBet}>
                        <RemoveCircleOutlineIcon sx={{fontSize: 10}}/>
                    </IconButton>
                </Grid>
                <Grid item xs={11} sx={{pr:1, pl:1}}>
                    <Box>
                        <Grid container>
                            <Grid item xs={9}>
                                {props.bet.vanity.main}
                            </Grid>
                            <Grid container justifyContent={"flex-end"} item xs={3}>
                                {props.bet.vanity.line}
                            </Grid>
                        </Grid>
                        
                    </Box>
                    <Box>
                        {props.bet.vanity.secondary}
                        
                    </Box>
                    <Box sx={{fontSize:10}}>
                        {props.bet.vanity.teams}
                    </Box>
                </Grid>
            </Grid>
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