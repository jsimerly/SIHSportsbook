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
    
    const re = /^[1-9]\d*(?:\.\d{0,2})?$/;
        
    function handleWager(e) {
        if (e.target.value==='' || re.test(e.target.value)) {
            setWager(e.target.value)


        }
    }

    function handleToWin(e){
        if (e.target.value==='' || re.test(e.target.value)) {
            setToWin(e.target.value)
        }
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
                            <InputLabel htmlFor="outlined-adornment-amount">To Win</InputLabel>
                            <OutlinedInput
                                size="small"
                                inputMode="numberic"
                                id="outlined-adornment-amount"
                                value={wager}
                                onChange={handleWager}
                                startAdornment={<InputAdornment position="start">$</InputAdornment>}
                                label="toWin"
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