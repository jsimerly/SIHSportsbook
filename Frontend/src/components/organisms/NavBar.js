import React, { Component } from "react";
import { 
    AppBar,
    Toolbar,
    Grid,
    Tabs,
    Tab
 } from '@mui/material';

export default function NavBar(props){
    return (
        <div>
            <AppBar>
                <Toolbar>
                    <Grid container>
                        <Grid item xs={3} md={3}>
                            LOGO HERE
                        </Grid>
                        <Grid item xs={6} md={6} justifyContent="center" style={{display:'flex'}}>
                            <Tabs>
                                <Tab label='Sportsbook'/>
                                <Tab label='League'/>
                                <Tab label='Stats'/>
                            </Tabs>
                        </Grid>
                        <Grid item xs={3} md={3} justifyContent='flex-end' style={{display:'flex'}}>
                            Log In - Sign Up
                        </Grid>
                    </Grid>

                </Toolbar>
            </AppBar>
        </div>
    )
}