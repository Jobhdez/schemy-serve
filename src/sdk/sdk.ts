class SDK {
  private url: string = "http://127.0.0.1:8000/api/";
  private register_url: string = "register/";
  private register_app_url: string = "users/apps/";
  constructor(
    username: string,
    password: string,
    first_name: string,
    email: string,
  ) {
    this.username = username;
    this.password = password;
    this.first_name = first_name;
    this.first_name = email;
  }
  public register() {
    const data = new URLSearchParams();
    data.append("password", this.password);
    data.append("password2", this.password);
    data.append("username", this.username);
    data.append("first_name", this.first_name);
    data.append("email", this.email);

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

  public register_app() {
    fetch(this.url + this.register_app_url, {
      method: "POST",
      headers: {
        Authorization: "Basic " + btoa(`${this.username}:${this.password}`),
      },
    })
      .then((response: Response) => response.json())
      .then((data: any) => {
        console.log(JSON.stringify(data));
      });
  }
}

let sdk = new SDK();
//sdk.register("venom", "123", "venom", "venom@gmail.com");
sdk.register_app("venom", "123");
