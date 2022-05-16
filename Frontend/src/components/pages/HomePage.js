import React, { Component } from "react";
import { render } from "react-dom";
import DrawerComp from "../organisms/Drawer";
import Matchups from "../organisms/Matchups";
import MatchUp from "../molecules/MatchUp";
import BetSlip from "../organisms/BetSlip";
import {
    Box,
    Grid
} from '@mui/material'


export default function App(props){
    return (
        <div>
            <Grid container>
                <Grid item>
                    <Box sx={{width: 250, height: '100vh', border:1 }}>
                        <DrawerComp/>
                    </Box>
                </Grid>
                <Grid margin={2} md={7} spacing={1} sx={{border:1}}>
                    <Matchups/>
                </Grid>
                <Grid margin={2} md={2} spacing={1} sx={{border:1}}>
                    <BetSlip/>
                </Grid>
            </Grid>
        </div>
    )
}