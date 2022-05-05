import React, { Component } from "react";
import { render } from "react-dom";
import DrawerComp from "../organisms/Drawer";
import Matchups from "../organisms/Matchups";
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
                <Grid item>
                    <Matchups/>
                </Grid>
            </Grid>
        </div>
    )
}