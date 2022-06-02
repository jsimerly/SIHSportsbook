import { Drawer, ListItem } from "@mui/material";
import React, { Component } from "react";
import { Box } from "@mui/system";
import { Divider } from "@mui/material";
import { List } from "@mui/material";

import LeagueButton from "../atoms/LeagueButton";

const drawerWidth = 240;

export default function DrawerComp(props){
    

    const drawer = (
        <div>
            
                {props.leagues.map((league, index) => {
                    return (
                        <LeagueButton 
                            leagueName={league.leagueName}
                            teamName={league.team}
                        />
                    )
                })}
          
            <Divider/>
            <List>
                {['Open Bet 1', 'Open Bet 2', 'Open Bet 3', 'Open Bet 4'].map((bet, index) => 
                    <ListItem>
                        {bet}
                    </ListItem>
                )}
            </List>
            <Divider/>
            <List>
                {['Won Bet', 'Lost Bet', 'Won Bet', 'Won Bet'].map((bet, index) => 
                    <ListItem>
                        {bet}
                    </ListItem>
                )}
            </List>
        </div>
    )
        
    return (
    <Box>
        {drawer}
    </Box>
    )
}
  