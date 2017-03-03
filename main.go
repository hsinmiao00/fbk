package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"

	fb "github.com/huandu/facebook"
)

type Friend struct {
	Name string
	Id   string
}

type Friends struct {
	Data []Friend
}

type Result struct {
	Friends Friends
}

type Config struct {
	User  string
	Token string
}

func main() {
	configRaw, _ := ioutil.ReadFile("conf.json")
	var config Config
	json.Unmarshal(configRaw, &config)

	res, _ := fb.Get("/"+config.User+"?fields=friends", fb.Params{
		"access_token": config.Token,
	})
	b, _ := json.Marshal(res)
	var r Result
	json.Unmarshal(b, &r)

	for _, f := range r.Friends.Data {
		fRes, _ := fb.Get("/"+f.Id+"?fields=posts", fb.Params{
			"access_token": config.Token,
		})
		posts, _ := json.Marshal(fRes)
		fmt.Println(string(posts))
	}
}
