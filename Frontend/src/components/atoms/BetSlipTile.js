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
    const [wager, setWager] = useState()
    const [toWin, setToWin] = useState()
    const line = props.bet.betData.line
    
    const re = /^[0-9]\d*(?:\.\d{0,2})?$/;
        
    function handleWager(e) {
        console.log(e.target.value)
        if (e.target.value==='' || re.test(e.target.value)) {
            setWager(e.target.value)
            console.log("made it in")
            let winAmount = 0

            if (line > 0) {
               winAmount = line/100 * e.target.value
            } else {
                winAmount = 100/(-1*line) * e.target.value
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
               betAmount = (e.target.value * 100)/line
            } else {
                betAmount = (e.target.value * line * -1)/100
            }

            betAmount = parseFloat(betAmount).toFixed(2)
            setWager(betAmount)
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
                    <Grid item xs={4} sx={{mr:1, mb:2}}>
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
                    <Grid item xs={4} sx={{ml:1, mb:2}}>
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