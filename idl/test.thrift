namespace py com.test

struct pos{
    1: required i32 x;
    2: required i32 y;
}

service posResp{
    double get_length(1:pos pos)
}