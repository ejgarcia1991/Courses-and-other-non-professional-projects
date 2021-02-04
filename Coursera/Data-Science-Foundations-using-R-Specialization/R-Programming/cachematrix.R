##It creates a list that serves as an object container in R
## That way you can use set or get functions to work with that function

makeCacheMatrix <- function(x = matrix()) {
  matrixCache<-NULL
  set<-function(y){
    x<<-y
    matrixCache<<-NULL
  }
  get<-function() x
  setMatrixCache<-function(mCache) matrixCache<<-mCache
  getMatrixCache<-function() matrixCache
  list(set = set, get = get,
       setMatrixCache = setMatrixCache,
       getMatrixCache = getMatrixCache)
}

cacheSolve <- function(x, ...) {
  m <- x$getMatrixCache()
  if(!is.null(m)) {
    message("getting cached data")
    return(m)
  }
  data <- x$get()
  m <- solve(data, ...) %*% data
  x$setMatrixCache(m)
  m
}

#Test code

m<-makeCacheMatrix()
m$set(matrix(c(4,7,3,4,5,6,7,8,9),nrow=3))

cacheSolve(m)
m$getMatrixCache()
cacheSolve(m)