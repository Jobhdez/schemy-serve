class SDK {
  private url: string = "http://127.0.0.1:8000/api/";
  private register_url: string = "register/";

  public register(
    username: string,
    password: string,
    first_name: string,
    email: string,
  ) {
    const data = new URLSearchParams();
    data.append("password", password);
    data.append("password2", password);
    data.append("username", username);
    data.append("first_name", first_name);
    data.append("email", email);

    fetch(this.url + this.register_url, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: data.toString(),
      // mode: "cors",
    })
      .then((response: Response) => response.json())
      .then((data: any) => {
        console.log(JSON.stringify(data));
      });
  }
}

let sdk = new SDK();
sdk.register("venom", "123", "venom", "venom@gmail.com");
