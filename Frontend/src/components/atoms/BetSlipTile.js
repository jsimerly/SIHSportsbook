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

    useEffect(() => {
    }, [wager])

    const currencyRegex = /(?=.*?\d)^\$?(([1-9]\d{0,2}(,\d{3})*)|\d+)?(\.\d{1,2})?$/;

    function handleWager(e) {
        // const value = e.target.value
        // let newWager = 0
        // console.log(1)
        // if (Number.isNaN(Number(value))) {
        //     console.log(2)
        //     newWager = wager
        // } else {
        //     const wagerValue = parseFloat(e.target.value).toFixed(2)
        //     console.log(3)
        //     console.log(wagerValue)
        //     if (currencyRegex.test(wagerValue)){
        //         console.log(4)
        //         newWager = wagerValue
        //     } else {
        //         console.log(5)
        //         newWager = wager
        //     }
        // }
        // setWager(...newWager)
    }

    function handleToWin(e){
        setToWin(e.target.value)
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
                                <InputLabel htmlFor="outlined-adornment-amount">Wager</InputLabel>
                                <OutlinedInput
                                    size="small"
                                    id="outlined-adornment-amount"
                                    value={wager}
                                    onChange={handleWager}
                                    startAdornment={<InputAdornment position="start">$</InputAdornment>}
                                    label="Wager"
                                />
                            </FormControl>
                        </Grid>
                        <Grid item xs={4} sx={{ml:1, mb:2}}>
                            <FormControl>
                                <InputLabel htmlFor="outlined-adornment-amount">To Win</InputLabel>
                                <OutlinedInput
                                    size="small"
                                    inputMode="numberic"
                                    id="outlined-adornment-amount"
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