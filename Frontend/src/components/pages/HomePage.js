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
                <Grid margin={2} md={7} sx={{border:1}}>
                    <Grid sx={{border:1, margin:1}}>
                        <Grid container columns={20}>
                            <Grid item md={8} sx={{border:1, padding:2}}>
                                test 20
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                        </Grid>
                        <Grid container columns={20}>
                            <Grid item md={8} sx={{border:1, padding:2}}>
                                test 1
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                        </Grid>
                    </Grid>
                    <Grid sx={{border:1, margin:1}}>
                        <Grid container columns={20}>
                            <Grid item md={8} sx={{border:1, padding:2}}>
                                test 20
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                        </Grid>
                        <Grid container columns={20}>
                            <Grid item md={8} sx={{border:1, padding:2}}>
                                test 1
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                        </Grid>
                    </Grid>
                    <Grid sx={{border:1, margin:1}}>
                        <Grid container columns={20}>
                            <Grid item md={8} sx={{border:1, padding:2}}>
                                test 20
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                        </Grid>
                        <Grid container columns={20}>
                            <Grid item md={8} sx={{border:1, padding:2}}>
                                test 1
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                            <Grid item md={4} sx={{border:1, padding:2}}>
                                test 2
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
            
        </div>
    )
}