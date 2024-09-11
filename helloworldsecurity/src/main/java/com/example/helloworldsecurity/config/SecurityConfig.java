package com.example.helloworldsecurity.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import static org.springframework.security.config.Customizer.withDefaults;

@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests(auth -> auth
                        .requestMatchers("/hello").authenticated() // Only authenticated users can access /hello
                        .anyRequest().permitAll() // All other endpoints are publicly accessible
                )
                .formLogin(withDefaults()) // Enable form-based login with default settings
                .httpBasic(withDefaults()); // Optional: Enables basic auth (you can remove this if only form-based login is required)

        return http.build();
    }

    @Bean
    public UserDetailsService userDetailsService() {
        UserDetails user = User.withUsername("test")
                .password("{noop}123456") // {noop} disables password encoding for simplicity
                .roles("USER")
                .build();
        return new InMemoryUserDetailsManager(user);
    }
}