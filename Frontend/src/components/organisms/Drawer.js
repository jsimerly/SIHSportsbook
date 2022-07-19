import { Drawer, ListItem } from "@mui/material";
import React, { Component, useEffect } from "react";
import { Box } from "@mui/system";
import { Divider } from "@mui/material";
import { List } from "@mui/material";

import LeagueButton from "../atoms/LeagueButton";
import LeagueHeader from "../molecules/LeagueHeader";
import PlacedBets from "../molecules/PlacedBets";

const drawerWidth = 240;

export default function DrawerComp(props){
    console.log(props.openBets)
    const drawer = (
        <div>
            <LeagueHeader/>
                {props.leagues.map((league, index) => {
                    return (
                        <LeagueButton 
                            league={league}
                            setLeague={props.setLeague}
                        />
                    )
                })}
          
            <Divider/>
            <List>
                {props.openBets.map((bet, index) => 
                    <PlacedBets bet={bet}/>
                )}
            </List>
            <Divider/>
            <List>
                {props.closedBets.map((bet, index) => 
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
  