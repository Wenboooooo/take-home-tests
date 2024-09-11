package com.example.helloworldsecurity.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.User;

@RestController
public class HelloWorldController {

    @GetMapping("/hello")
    public String helloWorld(@AuthenticationPrincipal User user) {
        return "Hello World, " + user.getUsername();
    }
}



