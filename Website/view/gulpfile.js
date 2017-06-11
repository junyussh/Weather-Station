var gulp = require('gulp');
var connect = require('gulp-connect');
var sass = require("gulp-sass");
gulp.task('server', function() {
    connect.server({
        livereload: true,
    });
});
gulp.task('sass', function() {
  gulp.src('assets/sass/*.scss')
      .pipe(sass({
          outputStyle: '',
          sourceMap: false,
          sourceMapContents: false,
          includePaths: ['node_modules/susy/sass']
      }).on('error', sass.logError))
      .pipe(gulp.dest('assets/css'))
      .pipe(connect.reload());
});
gulp.task('html', function() {
    gulp.src('*.html')
        .pipe(connect.reload());
});
gulp.task('watch',function(){
    gulp.watch('assets/sass/*.scss',['sass']);
    gulp.watch("*.html", ["html"])
});

gulp.task('default',['watch',"server", "sass"]);
