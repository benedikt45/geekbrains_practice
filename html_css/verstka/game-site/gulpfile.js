var gulp = require('gulp');
var gulpLess = require('gulp-less');

gulp.task('less', function(done) {
  gulp.src('./less/*.less')
    .pipe(gulpLess().on('error', less.logError))
    .pipe(gulp.dest('./css/'));
    done();
});

gulp.task('less:watch', function(){
  gulp.watch('less/*.less', function(e) {
    gulp.src(e.src)
      .pipe(gulpLess())
      .pipe(gulp.dest('./css/'));
      // done();
  });
});
